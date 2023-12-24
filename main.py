import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))
import json
print(json.dumps({"name": "John", "age": 30}))