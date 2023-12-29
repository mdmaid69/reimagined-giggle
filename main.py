import array
def convert_array_to_unicode(array):
        return array.tounicode()
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)