import math
def calculate_hyperbolic_arc_tangent(x):
        return math.atanh(x)
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)