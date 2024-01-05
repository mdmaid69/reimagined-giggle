import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)
import math
def calculate_cube_root(x):
        return math.pow(x, 1/3)