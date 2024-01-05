import math
def calculate_cone_volume(radius, height):
        return 1/3 * math.pi * radius**2 * height
import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)