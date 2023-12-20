import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)
list1 = [1, 2, 3]
list2 = [2, 3, 4]
print("Difference:", set(list1) - set(list2))