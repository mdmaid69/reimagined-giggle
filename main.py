import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)
import math
def calculate_bessel_function_of_second_kind(n, x):
        return math.yn(n, x)