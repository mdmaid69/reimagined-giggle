import math
def calculate_logarithm_base_2(x):
        return math.log2(x)
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)