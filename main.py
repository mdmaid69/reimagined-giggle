import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)
import math
def calculate_bessel_function_of_second_kind(n, x):
        return math.yn(n, x)