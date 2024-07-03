#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Read localised message content strings from translations/messages.<lang>.yaml
# files and use them to replace the corresponding strings in prelude.yaml.
import math
import re
import os

import yaml

messages = {}
for f in os.scandir('translations'):
    match = re.match(r'messages\.([^\.]+)\.yaml', f.name)
    if match:
        lang = match.group(1)
        with open(f.path, encoding='utf8') as input:
            messages[lang] = yaml.safe_load(input)

lines = []
with open('prelude.yaml', encoding='utf8') as input:
    lines = input.readlines()

    anchor = None
    lang = None
    for index, line in enumerate(lines):
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
        if match != None and anchor and lang:
            # Replace line with a new line for this message
            message = yaml.dump(messages[lang][anchor], width=math.inf, allow_unicode=True, default_style="'")

            lines[index] = re.sub(r' text: \'.+\'', f' text: {message.strip()}', line)


with open('prelude.yaml', mode='w', encoding='utf8') as output:
    output.writelines(lines)
