import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)