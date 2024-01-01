import json
def read_from_json(json_string):
        return json.loads(json_string)
import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}