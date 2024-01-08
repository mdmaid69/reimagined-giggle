import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)