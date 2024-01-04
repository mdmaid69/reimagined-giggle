import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)
import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)