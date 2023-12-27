import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)
import math
def calculate_sphere_volume(radius):
        return 4/3 * math.pi * radius**3