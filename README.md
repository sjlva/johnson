# Johnson

A pretty .json viewer

## Where to get it

The source code is currently hosted on Github at: https://github.com/sjlva/johnson 

Binary installers for the latest version are available at the https://pypi.org/project/johnson/ 

```bash
pip install jhonson
```

## Usage

`johnson --help` returns all commands available.

`johnson --file {file.json}` pretty prints on screen the {file.json} file.

`--indent` or `-i` sets the indent level (default is 4 spaces).

`--paging` or `--no-paging` enables / disables paging navigation through file (default is --no-paging). **Note:** Since the default pager on most platforms do not support color. Johnson will strip color from the output.
