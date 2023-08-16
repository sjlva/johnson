import json

from pytest import raises

from johnson.read_json import check_if_file_exists, read_json_file


def test_file_not_exist():

    path_to_file = '../inexistent_path/inexistent_file.json'
    file_exists = check_if_file_exists(path_to_file)

    assert file_exists is False


def test_file_exist():

    path_to_file = '../sample_jsons/example_1.json'
    file_exists = check_if_file_exists(path_to_file)

    assert file_exists is True


def test_read_inexistent_json():

    path_to_file = '../inexistent_path/inexistent_file.json'
    json_file = read_json_file(path_to_file)

    assert json_file is None


def test_read_valid_json():

    path_to_file = '../sample_jsons/example_1.json'
    json_file = read_json_file(path_to_file)

    assert json_file == {'key_1': 'value_1'}


def test_read_invalid_json():

    path_to_file = '../sample_jsons/example_1_invalid.json'
    error_message = 'Expecting value: line 2 column 12 (char 13)'

    with raises(json.decoder.JSONDecodeError) as error:
        json_file = read_json_file(path_to_file)

    assert error_message == error.value.args[0]
