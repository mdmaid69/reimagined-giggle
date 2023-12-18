import collections
def create_stack():
        return collections.deque()
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)