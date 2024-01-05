import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)
import math
def calculate_combinations(n, k):
        return math.comb(n, k)