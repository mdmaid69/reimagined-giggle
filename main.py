import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)
def find_common_elements(list1, list2):
        return set(list1) & set(list2)