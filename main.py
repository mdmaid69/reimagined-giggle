import json
print(json.dumps({"name": "John", "age": 30}))
import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))