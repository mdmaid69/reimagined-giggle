import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)
import math
def calculate_hypotenuse(a, b):
        return math.sqrt(a**2 + b**2)