import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)
import math
def calculate_product_of_sequence(start, stop, step):
        return math.prod(range(start, stop, step))