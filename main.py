import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)
import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))