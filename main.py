import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)
import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}