def find_min(numbers):
        return min(numbers)
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)