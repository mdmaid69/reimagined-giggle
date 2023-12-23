import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)