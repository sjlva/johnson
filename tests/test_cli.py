from typer.testing import CliRunner

from johnson.cli import app

runner = CliRunner()


def test_app_returns_0():
    file = '../sample_jsons/example_1.json'
    result = runner.invoke(app, ['--file', file])

    assert result.exit_code == 0


def test_json_contains_keys():
    file = '../sample_jsons/example_1.json'
    result = runner.invoke(app, ['--file', file])

    assert 'key_1' in result.stdout


def test_json_contains_values():
    file = '../sample_jsons/example_1.json'
    result = runner.invoke(app, ['--file', file])

    assert 'value_1' in result.stdout
