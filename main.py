import math
def calculate_degrees_to_radians(degrees):
        return math.radians(degrees)
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)