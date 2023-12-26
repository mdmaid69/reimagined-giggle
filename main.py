import math
def calculate_gamma_function(x):
        return math.gamma(x)
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)