import math
def calculate_euclidean_norm(v):
        return math.hypot(*v)
import json
def read_from_json(json_string):
        return json.loads(json_string)