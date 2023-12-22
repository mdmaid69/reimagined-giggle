import json
def convert_to_json(data):
        return json.dumps(data)
import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))