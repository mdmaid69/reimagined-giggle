import array
def get_array_as_complex(array):
        return complex(array[0])
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)