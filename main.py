import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))
import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)