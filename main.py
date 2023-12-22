import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
import json
def read_from_json(json_string):
        return json.loads(json_string)