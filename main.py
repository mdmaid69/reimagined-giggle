import math
def calculate_neper_number_to_power_x(x):
        return math.exp(x)
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)