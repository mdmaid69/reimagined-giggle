import json
def convert_to_json(data):
        return json.dumps(data)
import collections
def count_elements(iterable):
        return collections.Counter(iterable)