import json
def read_from_json(json_string):
        return json.loads(json_string)
import math
def calculate_polar_to_cartesian_coordinates(r, theta):
        return math.polar((r, theta))