import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)
import math
def calculate_pythagorean_theorem(a, b):
        return math.sqrt(a**2 + b**2)