import math
def calculate_logarithm_base_10(x):
        return math.log10(x)
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)