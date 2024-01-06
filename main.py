import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)
import array
def check_if_array_does_not_contain_item(array, item):
        return item not in array