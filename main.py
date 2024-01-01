import math
def calculate_factorial(n):
        return math.factorial(n)
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)