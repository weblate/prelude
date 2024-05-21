import math
import re

from yaml import dump

# This makes some assumptions about the prelude.yaml:
# - anchors are always separated from anything before them by at least one space
# - message content objects are listed with the lang as the first key, followed
#   by the text
# - message content text is enclosed in single quotes

messages = {}
with open('prelude.yaml', encoding='utf8') as input:
    lines = input.readlines()

    anchor = None
    lang = None
    for line in lines:
        match = re.search(r' &([^\s]+)$', line)
        if match != None:
            anchor = match.group(1)
            lang = None
            text = None
            continue

        match = re.search(r'- lang: ([a-zA-Z_]+)', line)
        if match != None:
            lang = match.group(1)
            text = None
            continue

        match = re.search(r' text: \'(.+)\'', line)
        if match != None:
            text = match.group(1).replace("''", "'")

        if anchor and lang and text:
            if lang in messages:
                messages[lang][anchor] = text
            else:
                messages[lang] = { anchor: text }

for lang in messages:
    with open(f'translations/messages.{lang}.yaml', mode='w', encoding='utf8') as output:
        dump({ 'messages': messages[lang] }, output, allow_unicode=True, width=math.inf)
