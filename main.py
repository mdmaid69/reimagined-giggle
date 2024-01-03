import math
def calculate_inverse_hyperbolic_cosine(x):
        return math.acosh(x)
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)