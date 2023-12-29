import math
def calculate_floor(x):
        return math.floor(x)
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)