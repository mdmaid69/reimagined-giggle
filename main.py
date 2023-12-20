import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)
import json
def convert_to_json(data):
        return json.dumps(data)