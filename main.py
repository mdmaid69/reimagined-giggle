import math
def calculate_logarithm_base_e(x):
        return math.log(x)
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)