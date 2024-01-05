import json
def convert_to_json(data):
        return json.dumps(data)
import math
def calculate_product_of_sequence(start, stop, step):
        return math.prod(range(start, stop, step))