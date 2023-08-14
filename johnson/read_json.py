import json
import os.path


def read_json_file(path_to_file: str) -> dict:
    """
    Reads a json file from a given path.

    Parameters:
        path_to_file: path to json file

    Returns:
        A dict with json data

    Examples:
        >>> read_json_file('../sample_jsons/example_1.json')
        {'key_1': 'value_1'}
    """

    current_directory = os.path.dirname(__file__)
    file_path = os.path.join(current_directory, path_to_file)

    with open(file_path, 'r') as file:
        data = json.load(file)

    return data
