import math
def calculate_hyperbolic_cosine(x):
        return math.cosh(x)
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)