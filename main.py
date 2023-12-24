import json
def read_from_json(json_string):
        return json.loads(json_string)
import math
def calculate_sign(x):
        return math.copysign(1, x)