import json
def read_from_json(json_string):
        return json.loads(json_string)
import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))