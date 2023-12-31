import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)
import math
def calculate_root(x, n):
        return math.pow(x, 1/n)