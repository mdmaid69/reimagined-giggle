import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)
import math
def calculate_neper_number_to_power_x(x):
        return math.exp(x)