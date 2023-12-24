import json
def convert_to_json(data):
        return json.dumps(data)
import math
def calculate_bessel_function_of_first_kind(n, x):
        return math.jn(n, x)