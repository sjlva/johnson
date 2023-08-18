# Johnson

![CI](https://github.com/sjlva/johnson/actions/workflows/pipeline.yaml/badge.svg) [![codecov](https://codecov.io/gh/sjlva/johnson/graph/badge.svg?token=VWQWIP5GCM)](https://codecov.io/gh/sjlva/johnson) [![Documentation Status](https://readthedocs.org/projects/pyjohnson/badge/?version=latest)](https://pyjohnson.readthedocs.io/en/latest/?badge=latest)

Pretty print .json data in your terminal

## Installing

Install and update using pip:

```bash
pip install -U johnson
```

## Usage

+ Pretty print your json file

```bash
johnson -f '../example.json'
```

```bash
{
  "glossary": {
    "title": "example glossary",
    "GlossDiv": {
      "title": "S",
      "GlossList": {
        "GlossEntry": {
          "ID": "SGML",
          "SortAs": "SGML",
          "GlossTerm": "Standard Generalized Markup Language",
          "Acronym": "SGML",
          "Abbrev": "ISO 8879:1986",
          "GlossDef": {
            "para": "A meta-markup language, used to create markup languages such as DocBook.",
            "GlossSeeAlso": [
              "GML",
              "XML"
            ]
          },
          "GlossSee": "markup"
        }
      }
    }
  }
}
```

+ See all commands available

```bash
poetry run johnson --help
```

```bash
 Usage: johnson [OPTIONS]

╭─ Options ─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ *  --file                -f      TEXT  path to json file [default: None] [required]                                               │
│    --install-completion                Install completion for the current shell.                                                  │
│    --show-completion                   Show completion for the current shell, to copy it or customize the installation.           │
│    --help                              Show this message and exit.                                                                │
╰───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
```



