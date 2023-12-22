import math
def calculate_absolute_value(x):
        return math.fabs(x)
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)