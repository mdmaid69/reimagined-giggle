import json
def convert_to_json(data):
        return json.dumps(data)
import array
def get_array_buffer_info(array):
        return array.buffer_info()