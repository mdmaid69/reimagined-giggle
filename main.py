import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)
import json
def read_from_json(json_string):
        return json.loads(json_string)