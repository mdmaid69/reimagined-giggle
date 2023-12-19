import math
def calculate_combinations(n, k):
        return math.comb(n, k)
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)