import math
def calculate_tangent(x):
        return math.tan(x)
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)