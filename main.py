import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)
import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)