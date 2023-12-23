import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)
import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)