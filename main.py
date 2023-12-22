import json
print(json.dumps({"name": "John", "age": 30}))
import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)