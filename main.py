import json
def convert_to_json(data):
        return json.dumps(data)
def find_difference(list1, list2):
        return set(list1) - set(list2)