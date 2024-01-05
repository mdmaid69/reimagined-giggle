import math
def calculate_logarithm(base, x):
        return math.log(x, base)
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)