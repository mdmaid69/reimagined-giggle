import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
import json
def convert_to_json(data):
        return json.dumps(data)