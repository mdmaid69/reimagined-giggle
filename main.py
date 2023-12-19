import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)
import json
print(json.dumps({"name": "John", "age": 30}))