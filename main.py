import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)
import math
def calculate_cylinder_volume(radius, height):
        return math.pi * radius**2 * height