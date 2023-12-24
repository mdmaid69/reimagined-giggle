import json
print(json.dumps({"name": "John", "age": 30}))
def find_common_elements(list1, list2):
        return set(list1) & set(list2)