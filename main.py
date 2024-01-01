import json
def read_from_json(json_string):
        return json.loads(json_string)
import math
def calculate_bessel_function_of_second_kind(n, x):
        return math.yn(n, x)