import math
def calculate_euclidean_norm(v):
        return math.hypot(*v)
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)