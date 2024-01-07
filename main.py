import math
def calculate_product_of_sequence(start, stop, step):
        return math.prod(range(start, stop, step))
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)