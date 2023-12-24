import math
def calculate_combinations(n, k):
        return math.comb(n, k)
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)