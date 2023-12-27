import array
def get_array_buffer_info(array):
        return array.buffer_info()
import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)