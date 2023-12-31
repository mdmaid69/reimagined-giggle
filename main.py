import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)