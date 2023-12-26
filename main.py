import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)