import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)
import math
def calculate_euclidean_distance(p, q):
        return math.dist(p, q)