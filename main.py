import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)
import itertools
print(list(itertools.permutations([1, 2, 3])))