import math
def calculate_gamma_function(x):
        return math.gamma(x)
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)