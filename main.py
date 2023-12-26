def find_difference(list1, list2):
        return set(list1) - set(list2)
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)