import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)