import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)
import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)