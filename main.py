import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)
import math
def calculate_hyperbolic_arc_cosine(x):
        return math.acosh(x)