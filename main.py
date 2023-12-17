import json
def convert_to_json(data):
        return json.dumps(data)
import array
def get_array_as_memoryview(array):
        return memoryview(array)