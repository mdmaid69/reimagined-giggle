import collections
def create_priority_queue():
        return collections.deque()
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)