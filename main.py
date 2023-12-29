import math
def calculate_hyperbolic_cosine(x):
        return math.cosh(x)
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)