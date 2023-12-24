import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)
import array
def convert_array_to_unicode(array):
        return array.tounicode()