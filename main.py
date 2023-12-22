import json
def convert_to_json(data):
        return json.dumps(data)
import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))