import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)
import math
def calculate_radians_to_degrees(radians):
        return math.degrees(radians)