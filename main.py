import math
def calculate_tangent(x):
        return math.tan(x)
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)