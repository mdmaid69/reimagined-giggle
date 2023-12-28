import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)
import array
def get_array_as_format(array, format_spec):
        return format(array, format_spec)