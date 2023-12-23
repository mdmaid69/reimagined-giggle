import json
def read_from_json(json_string):
        return json.loads(json_string)
import array
def insert_into_array(array, i, item):
        array.insert(i, item)