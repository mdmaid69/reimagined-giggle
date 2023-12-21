import math
def calculate_bessel_function_of_first_kind(n, x):
        return math.jn(n, x)
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)