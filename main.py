import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)
import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))