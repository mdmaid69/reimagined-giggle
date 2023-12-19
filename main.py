import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)
import math
def calculate_inverse_hyperbolic_tangent(x):
        return math.atanh(x)