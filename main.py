import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)
import array
def get_array_buffer_info(array):
        return array.buffer_info()