import json
def convert_to_json(data):
        return json.dumps(data)
import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))