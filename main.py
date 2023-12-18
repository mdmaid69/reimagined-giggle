import json
def read_from_json(json_string):
        return json.loads(json_string)
import math
def calculate_sphere_volume(radius):
        return 4/3 * math.pi * radius**3