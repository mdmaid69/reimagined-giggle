import array
def get_array_as_float(array):
        return float(array[0])
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)