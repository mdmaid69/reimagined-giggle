import math
def calculate_inverse_hyperbolic_tangent(x):
        return math.atanh(x)
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)