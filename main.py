import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)
import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)