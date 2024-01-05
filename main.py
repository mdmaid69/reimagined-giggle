import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)
list1 = [1, 2, 3]
list2 = [2, 3, 4]
print("Difference:", set(list1) - set(list2))