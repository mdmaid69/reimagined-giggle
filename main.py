import math
def calculate_sine(x):
        return math.sin(x)
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)