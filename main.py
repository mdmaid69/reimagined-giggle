import array
def get_array_as_frozenset(array):
        return frozenset(array)
import json
def read_from_json(json_string):
        return json.loads(json_string)