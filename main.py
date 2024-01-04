def sort_numbers(numbers):
        return sorted(numbers)
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)