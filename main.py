import collections
def count_elements(iterable):
        return collections.Counter(iterable)
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)