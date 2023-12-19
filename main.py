import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)
import math
def calculate_floor(x):
        return math.floor(x)