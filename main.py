import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)