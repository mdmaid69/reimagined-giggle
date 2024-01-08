import json
def read_from_json(json_string):
        return json.loads(json_string)
import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)