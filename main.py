import json
def convert_to_json(data):
        return json.dumps(data)
import math
def calculate_cone_volume(radius, height):
        return 1/3 * math.pi * radius**2 * height