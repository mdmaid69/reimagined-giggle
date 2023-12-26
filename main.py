def is_odd(n):
        return n % 2 != 0
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)