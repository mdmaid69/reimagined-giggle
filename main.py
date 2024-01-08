import math
def calculate_hyperbolic_arc_tangent(x):
        return math.atanh(x)
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)