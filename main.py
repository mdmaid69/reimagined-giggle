import math
def calculate_logarithm_of_gamma_function(x):
        return math.lgamma(x)
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)