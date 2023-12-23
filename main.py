import json
def read_from_json(json_string):
        return json.loads(json_string)
import math
def calculate_cone_volume(radius, height):
        return 1/3 * math.pi * radius**2 * height