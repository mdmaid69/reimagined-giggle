import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)