import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)