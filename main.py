import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)
import math
def calculate_polar_to_cartesian_coordinates(r, theta):
        return math.polar((r, theta))