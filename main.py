import collections
def create_stack():
        return collections.deque()
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)