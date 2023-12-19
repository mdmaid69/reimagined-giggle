import array
def get_string_from_array(array):
        return array.tobytes()
import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)