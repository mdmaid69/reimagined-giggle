import json
def read_from_json(json_string):
        return json.loads(json_string)
import array
def get_array_slice(array, i, j):
        return array[i:j]