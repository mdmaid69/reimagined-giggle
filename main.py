import array
def get_list_from_array(array):
        return array.tolist()
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)