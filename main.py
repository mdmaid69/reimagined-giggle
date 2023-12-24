import math
def calculate_hyperbolic_sine(x):
        return math.sinh(x)
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)