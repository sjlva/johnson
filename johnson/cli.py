import typer
from rich import print_json
from rich.console import Console
from typer import Typer
from typing_extensions import Annotated

from johnson.read_json import read_json_file

console = Console()
app = Typer()


@app.command()
def johnson(file: Annotated[str, typer.Option('--file', '-f')]):

    data = read_json_file(file)

    console.print_json(data=data)
