import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)
import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))