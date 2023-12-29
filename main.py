import json
def convert_to_json(data):
        return json.dumps(data)
import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)