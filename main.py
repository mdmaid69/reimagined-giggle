import math
def calculate_power(base, exponent):
        return math.pow(base, exponent)
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)