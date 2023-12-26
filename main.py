import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)