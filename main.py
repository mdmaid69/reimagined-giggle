import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)
import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)