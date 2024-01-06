import array
def get_array_as_format(array, format_spec):
        return format(array, format_spec)
import json
def read_from_json(json_string):
        return json.loads(json_string)