import math
def calculate_arc_sine(x):
        return math.asin(x)
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)