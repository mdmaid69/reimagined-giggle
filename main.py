import collections
def count_elements(iterable):
        return collections.Counter(iterable)
import json
def read_from_json(json_string):
        return json.loads(json_string)