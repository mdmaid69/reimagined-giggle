import json
print(json.dumps({"name": "John", "age": 30}))
import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))