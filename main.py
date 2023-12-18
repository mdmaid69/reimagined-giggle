import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)
import json
def read_from_json(json_string):
        return json.loads(json_string)