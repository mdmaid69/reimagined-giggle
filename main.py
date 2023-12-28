import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)
import math
def calculate_sign(x):
        return math.copysign(1, x)