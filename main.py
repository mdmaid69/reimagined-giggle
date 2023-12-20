import array
def get_string_from_array(array):
        return array.tobytes()
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)