import math
def calculate_remainder(x, y):
        return math.remainder(x, y)
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)