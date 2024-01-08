import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)
import math
def calculate_hypotenuse(a, b):
        return math.sqrt(a**2 + b**2)