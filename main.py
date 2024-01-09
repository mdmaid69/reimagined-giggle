import json
def read_from_json(json_string):
        return json.loads(json_string)
import collections
def create_queue():
        return collections.deque()