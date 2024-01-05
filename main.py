import array
def reverse_array(array):
        array.reverse()
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)