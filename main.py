import math
def calculate_arc_tangent(x):
        return math.atan(x)
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)