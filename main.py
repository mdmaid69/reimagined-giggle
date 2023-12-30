import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)
import math
def calculate_cube_root(x):
        return math.pow(x, 1/3)