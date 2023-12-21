import array
def get_list_from_array(array):
        return array.tolist()
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)