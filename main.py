import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)
import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)