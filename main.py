import math
def calculate_logarithm(base, x):
        return math.log(x, base)
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)