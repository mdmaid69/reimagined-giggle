import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)
list1 = [1, 2, 3]
list2 = [2, 3, 4]
print("Difference:", set(list1) - set(list2))