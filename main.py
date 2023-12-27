import collections
def create_priority_queue():
        return collections.deque()
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)