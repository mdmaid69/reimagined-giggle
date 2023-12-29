import array
def convert_array_to_list(array):
        return array.tolist()
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)