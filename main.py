import math
def calculate_cylinder_volume(radius, height):
        return math.pi * radius**2 * height
import json
def read_from_json(json_string):
        return json.loads(json_string)