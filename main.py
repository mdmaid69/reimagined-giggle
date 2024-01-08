import math
def calculate_square_root(x):
        return math.sqrt(x)
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)