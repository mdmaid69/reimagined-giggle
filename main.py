import math
def calculate_euclidean_norm(v):
        return math.hypot(*v)
import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)