import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)
import math
def calculate_product_of_sequence(start, stop, step):
        return math.prod(range(start, stop, step))