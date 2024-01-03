import math
def calculate_hyperbolic_tangent(x):
        return math.tanh(x)
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)