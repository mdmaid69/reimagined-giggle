import json
def convert_to_json(data):
        return json.dumps(data)
import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)