from pathlib import Path
from typing import Optional

import typer
from rich import print_json
from rich.console import Console
from typer import Typer
from typing_extensions import Annotated

from johnson.read_json import read_json_file

console = Console()
app = Typer()


@app.command()
def johnson(
    file: Annotated[
        Optional[Path], typer.Option('--file', '-f', help='path to json file')
    ]
):

    if file is None:
        console.print('No json file')
        raise typer.Abort()
    if file.is_file():
        data = read_json_file(file)
        console.print_json(data=data)
    elif file.is_dir():
        console.print('Config is a directory, will use all its file files')
    elif not file.exists():
        console.print("The file doesn't exist")
