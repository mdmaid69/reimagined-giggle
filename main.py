import json
def convert_to_json(data):
        return json.dumps(data)
list1 = [1, 2, 3]
list2 = [2, 3, 4]
print("Union:", set(list1) | set(list2))