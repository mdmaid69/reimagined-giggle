import array
def get_array_buffer_info(array):
        return array.buffer_info()
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)