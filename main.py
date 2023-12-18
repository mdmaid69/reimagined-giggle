import math
def calculate_radians_to_degrees(radians):
        return math.degrees(radians)
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)