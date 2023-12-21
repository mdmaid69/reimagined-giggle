import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)
import math
def calculate_euclidean_distance(p, q):
        return math.dist(p, q)