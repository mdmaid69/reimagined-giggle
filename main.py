import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)
import math
def calculate_bessel_function_of_first_kind(n, x):
        return math.jn(n, x)