import math
def calculate_sine(x):
        return math.sin(x)
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)