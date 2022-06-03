import json
import typer
from rich.console import Console
from rich import print_json

app = typer.Typer(name="jhonson")

@app.command()
def cat(file_name: str = typer.Option(..., "--file", "-f"),
        indent: int = typer.Option(4, "--indent", "-i"),
        paging: bool = False):

    console = Console()
    with open(file_name, "r") as json_file:
        data = json.load(json_file)
        if not paging:
            console.print_json(data=data, indent=indent)
        else:
            with console.pager():
                console.print_json(data=data, indent=indent)

if __name__ == "__main__":
    app()


