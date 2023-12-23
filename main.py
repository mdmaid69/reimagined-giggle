import math
def calculate_euclidean_norm(v):
        return math.hypot(*v)
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)