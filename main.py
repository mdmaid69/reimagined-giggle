import array
def get_array_as_format(array, format_spec):
        return format(array, format_spec)
import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)