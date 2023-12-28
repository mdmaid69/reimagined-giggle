import math
def calculate_sign(x):
        return math.copysign(1, x)
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)