import array
def pop_from_array(array, i=-1):
        return array.pop(i)
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)