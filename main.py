import math
def calculate_error_function(x):
        return math.erf(x)
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)