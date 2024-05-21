# About

This repository holds the masterlist prelude, a metadata file that is used to supply common metadata to all masterlists.

See [CONTRIBUTING.md](CONTRIBUTING.md) for information on how to contribute to the prelude.

### Updating Weblate translations

The `translations` directory holds files that are read and written by Weblate. It's possible to regenerate their content from the `prelude.yaml` by running the following, assuming Python 3 is installed on Windows:

```
py -m venv .venv
.\venv\Scripts\activate
pip install -r requirements.txt
py extract-strings.py
```

It's also possible to overwrite the message text in `prelude.yaml` using the contents of the `translations` directory:

```
py -m venv .venv
.\venv\Scripts\activate
pip install -r requirements.txt
py import-strings.py
```
