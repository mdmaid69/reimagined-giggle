import collections
def group_by(iterable, key_func):
        return collections.defaultdict(list, ((key, list(group)) for key, group in itertools.groupby(sorted(iterable, key=key_func), key_func)))
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)