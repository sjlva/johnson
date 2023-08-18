import json


def read_json_file(path_to_file: str) -> dict:
    """
    Read a json file from a given path.

    Parameters:
        path_to_file: path to json file

    Returns:
        A dict with json data
    """

    with open(path_to_file, 'r') as file:
        try:
            data = json.load(file)
            return data
        except json.decoder.JSONDecodeError as e:
            raise e
