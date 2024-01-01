import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)
import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))