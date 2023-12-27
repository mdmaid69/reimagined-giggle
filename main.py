import math
def calculate_bessel_function_of_first_kind(n, x):
        return math.jn(n, x)
import json
def read_from_json(json_string):
        return json.loads(json_string)