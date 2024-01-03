import json
print(json.dumps({"name": "John", "age": 30}))
import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)