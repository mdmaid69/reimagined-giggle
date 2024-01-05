def find_difference(list1, list2):
        return set(list1) - set(list2)
import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)