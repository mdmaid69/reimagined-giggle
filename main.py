import itertools
print(list(itertools.permutations([1, 2, 3])))
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)