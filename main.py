import math
def calculate_arc_cosine(x):
        return math.acos(x)
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)