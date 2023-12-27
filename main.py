import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))
import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)