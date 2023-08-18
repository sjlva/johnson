from pytest import raises
from typer.testing import CliRunner

from johnson.cli import app

runner = CliRunner()


def test_app_returns_0():
    file = 'sample_jsons/example_1.json'
    result = runner.invoke(app, ['--file', file])

    assert result.exit_code == 0


def test_json_contains_keys_and_values():
    file = 'sample_jsons/example_1.json'
    result = runner.invoke(app, ['--file', file])

    assert 'key_1' in result.stdout
    assert 'value_1' in result.stdout


def test_json_is_none():
    file = ''

    result = runner.invoke(app, ['--file', file])

    assert result.exit_code == 1


def test_json_does_not_exist():
    file = 'sample_jsons/exle_1.json'
    result = runner.invoke(app, ['--file', file])

    assert result.exit_code == 1
