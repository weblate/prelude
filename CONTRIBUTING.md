Contributing To The Masterlist Prelude
======================================

## Filing Issues

If you're about to file an issue for some suggested change, please consider instead making the change yourself and submitting it as a pull request. Pull requests are much more likely to be quickly acted on, so they're the best way to get your change into the prelude.

## Making Changes

LOOT's masterlists as well as the prelude are [versioned](https://loot.github.io/docs/contributing/Masterlist-Versioning). Before making any changes, please make sure that you're working on the correct branch for LOOT's latest release.

If you are new to contributing to projects on GitHub, the [How To Contribute](https://loot.github.io/docs/contributing/How-To-Contribute) wiki page is a good starting point.

The format and syntax of the masterlist prelude is [fully documented](https://loot-api.readthedocs.io/en/stable/metadata/introduction.html), and other information on how to edit the masterlist prelude can be found on the [Masterlist Editing](https://loot.github.io/docs/contributing/Masterlist-Editing) wiki page.

If you send a pull request, then discover that you have made a mistake, feel free to make additional commits to fix it. You don't need to squash your commits or open a new pull request to keep your commit history tidy; whoever merges your pull request can squash it for you. You can also mark your pull request as a draft if it isn't ready to be merged.

### Testing Changes

Pull requests and all commits to the prelude repository are automatically run through a validator to check for syntax errors.

Nevertheless, it is advisable to test your changes on your own LOOT install before sending a pull request, as they may have valid syntax but not have the intended effect. Instructions on how to do so can be found on [LOOT's wiki](https://loot.github.io/docs/contributing/Quickly-Testing-Your-Masterlist-Changes).

### Translations

`prelude.yaml` contains localised messages that are used by LOOT, and the data structure used to localise messages in LOOT's metadata files (including the prelude) is described [here](https://loot-api.readthedocs.io/en/stable/metadata/data_structures/localised_content.html). The localized content data structures should be sorted alphabetically by locale code with the exception of `en` at the beginning since it is LOOT's default language.

The `translations` directory is used to integrating with [Weblate](https://hosted.weblate.org/projects/loot/prelude/) so that translations can be managed and maintained there. The `translations` directory contains `messages.<locale code>.yaml` files, where `<locale code>` is a POSIX locale code (see the table below for examples). Each file contains a map where the keys are anchor names and the values are the localised text for that language.

The anchor names correspond to the YAML anchors used for localised messages in `prelude.yaml`, but the contents of the `translations` directory are **not** automatically synchronised with `prelude.yaml`: that must be done manually by a maintainer. When adding a new message to the prelude, it's enough to add its anchor and English message to `translations/messages.en.yaml`: Weblate will then show it as a missing translation for all other languages.

**Note:** If adding a translation for a new language, you need to add support for it to LOOT before it will be usable: see [LOOT's contributing guide](https://github.com/loot/loot/blob/master/CONTRIBUTING.md#translating-loot) for more information.

| Locale Code | Language |
| ------------- | ----------- |
| `bg` | Bulgarian |
| `cs` | Czech |
| `da` | Danish |
| `de` | German |
| `es` | Spanish |
| `fi` | Finnish |
| `fr` | French |
| `it` | Italian |
| `ja` | Japanese |
| `ko` | Korean |
| `pl` | Polish |
| `pt_BR` | Portuguese (Brazil) |
| `pt_PT` | Portuguese |
| `ru` | Russian |
| `sv` | Swedish |
| `uk_UA` | Ukrainian |
| `zh_CN` | Chinese (Simplified) |
