import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)
import array
def clear_array(array):
        array *= 0