import array
def convert_array_to_unicode(array):
        return array.tounicode()
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)