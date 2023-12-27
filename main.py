import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)
import array
def iterate_over_array(array):
        for item in array:
        print(item)