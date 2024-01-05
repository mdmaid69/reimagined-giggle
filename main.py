list1 = [1, 2, 3]
list2 = [2, 3, 4]
print("Common elements:", set(list1) & set(list2))
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)