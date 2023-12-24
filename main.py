import math
def calculate_ceiling(x):
        return math.ceil(x)
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)