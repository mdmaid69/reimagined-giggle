import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)
import math
def calculate_logarithm_base_2(x):
        return math.log2(x)