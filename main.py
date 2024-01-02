import math
def calculate_sign(x):
        return math.copysign(1, x)
import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)