import math
def calculate_exponential(x):
        return math.exp(x)
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)