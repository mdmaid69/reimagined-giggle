import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)
import collections
def create_stack():
        return collections.deque()