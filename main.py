import math
def calculate_factorial(n):
        return math.factorial(n)
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)