import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)
import collections
def create_ordered_dict():
        return collections.OrderedDict()