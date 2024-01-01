import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)
import json
def read_from_json(json_string):
        return json.loads(json_string)