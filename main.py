import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)
import array
def get_bytes_from_array(array):
        return array.tobytes()