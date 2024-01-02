import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)
import json
def convert_to_json(data):
        return json.dumps(data)