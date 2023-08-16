import json
import os.path


def check_if_file_exists(path_to_file: str) -> bool:
    """
    Check if a file exists

    Parameters:
        path_to_file: path to json file

    Returns:
        A bool. True if json exists, False otherwise.

    Examples:
        >>> check_if_file_exists('../sample_jsons/example_1.json')
        True
        >>> check_if_file_exists('../inexistent_path/inexistent_file.json')
        False
    """

    file_path = parse_directory(path_to_file)
    file_exists = os.path.isfile(file_path)

    return file_exists


def parse_directory(path_to_file: str) -> str:
    """
    Parse the directory path of any given file

    Parameters:
        path_to_file: path to json file

    Returns:
        A string with parsed directory
    """

    current_directory = os.path.dirname(__file__)
    file_path = os.path.join(current_directory, path_to_file)

    return file_path


def read_json_file(path_to_file: str) -> dict:
    """
    Read a json file from a given path.

    Parameters:
        path_to_file: path to json file

    Returns:
        A dict with json data

    Examples:
        >>> read_json_file('../sample_jsons/example_1.json')
        {'key_1': 'value_1'}
    """

    json_exists = check_if_file_exists(path_to_file)

    if json_exists:
        file_directory = parse_directory(path_to_file)

        with open(file_directory, 'r') as file:
            try:
                data = json.load(file)
                return data
            except json.decoder.JSONDecodeError as e:
                raise e

    else:
        print(f'File {path_to_file} not found.')
        return None
