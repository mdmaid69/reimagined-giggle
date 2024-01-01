import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))
import json
def read_from_json(json_string):
        return json.loads(json_string)