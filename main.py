import math
def calculate_square_root(x):
        return math.sqrt(x)
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)