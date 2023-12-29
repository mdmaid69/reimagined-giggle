def find_common_elements(list1, list2):
        return set(list1) & set(list2)
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)