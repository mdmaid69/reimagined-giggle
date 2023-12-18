import collections
def create_ordered_dict():
        return collections.OrderedDict()
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)