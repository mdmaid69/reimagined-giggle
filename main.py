import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}
import json
def convert_to_json(data):
        return json.dumps(data)