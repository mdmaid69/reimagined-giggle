import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)
import collections
def count_elements(iterable):
        return collections.Counter(iterable)