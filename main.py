import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))
import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)