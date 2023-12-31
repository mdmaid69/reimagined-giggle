import math
def calculate_exponential(x):
        return math.exp(x)
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)