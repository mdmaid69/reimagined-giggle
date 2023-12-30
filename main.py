import array
def extend_array(array, iterable):
        array.extend(iterable)
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)