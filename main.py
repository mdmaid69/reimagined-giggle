import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)
import math
def calculate_remainder(x, y):
        return math.remainder(x, y)