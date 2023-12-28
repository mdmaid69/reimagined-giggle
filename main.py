import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)
import math
def calculate_greatest_common_divisor(a, b):
        return math.gcd(a, b)