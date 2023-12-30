import array
def get_array_as_format(array, format_spec):
        return format(array, format_spec)
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)