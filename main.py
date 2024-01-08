import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)
import array
def get_array_item_count(array, item):
        return array.count(item)