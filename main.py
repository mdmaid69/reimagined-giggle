import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)
import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)