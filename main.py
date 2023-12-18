import collections
def group_by(iterable, key_func):
        return collections.defaultdict(list, ((key, list(group)) for key, group in itertools.groupby(sorted(iterable, key=key_func), key_func)))
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)