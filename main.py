import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)
import math
def calculate_absolute_value(x):
        return math.fabs(x)