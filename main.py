import math
def calculate_inverse_hyperbolic_sine(x):
        return math.asinh(x)
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)