import math
def calculate_hyperbolic_tangent(x):
        return math.tanh(x)
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)