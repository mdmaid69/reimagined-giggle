import json
def read_from_json(json_string):
        return json.loads(json_string)
list1 = [1, 2, 3]
list2 = [2, 3, 4]
print("Common elements:", set(list1) & set(list2))