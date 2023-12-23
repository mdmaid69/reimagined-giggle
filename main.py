def find_max(numbers):
        return max(numbers)
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)