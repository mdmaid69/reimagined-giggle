import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)
import array
def iterate_over_array(array):
        for item in array:
        print(item)