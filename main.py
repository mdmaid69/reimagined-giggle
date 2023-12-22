import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))
import json
def read_from_json(json_string):
        return json.loads(json_string)