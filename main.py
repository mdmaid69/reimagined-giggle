import math
def calculate_product_of_sequence(start, stop, step):
        return math.prod(range(start, stop, step))
import json
def read_from_json(json_string):
        return json.loads(json_string)