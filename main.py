import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)
import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))