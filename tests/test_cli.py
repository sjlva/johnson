from pathlib import Path

from pytest import raises
from typer.testing import CliRunner

from johnson.cli import app

test_data_dir = Path(__file__).parent / 'sample_jsons'
runner = CliRunner()


def test_app_returns_0():
    file = f'{test_data_dir}/example_1.json'
    result = runner.invoke(app, ['--file', file])

    assert result.exit_code == 0


def test_json_contains_keys_and_values():
    file = f'{test_data_dir}/example_1.json'
    result = runner.invoke(app, ['--file', file])

    assert 'key_1' in result.stdout
    assert 'value_1' in result.stdout


def test_json_is_none():
    file = ''

    result = runner.invoke(app, ['--file', file])

    assert result.exit_code == 1


def test_json_does_not_exist():
    file = f'{test_data_dir}/expsdlf_.json'
    result = runner.invoke(app, ['--file', file])

    assert result.exit_code == 1
