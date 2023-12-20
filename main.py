import json
def convert_to_json(data):
        return json.dumps(data)
import collections
def create_queue():
        return collections.deque()