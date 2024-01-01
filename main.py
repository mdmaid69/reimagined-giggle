import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)
def find_union(list1, list2):
        return set(list1) | set(list2)