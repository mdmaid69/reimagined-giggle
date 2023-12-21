import math
def calculate_greatest_common_divisor(a, b):
        return math.gcd(a, b)
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)