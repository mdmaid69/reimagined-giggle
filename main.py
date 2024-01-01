import collections
def create_ordered_dict():
        return collections.OrderedDict()
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)