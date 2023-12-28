import math
def calculate_arc_sine(x):
        return math.asin(x)
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)