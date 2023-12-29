import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)
import math
def calculate_cone_volume(radius, height):
        return 1/3 * math.pi * radius**2 * height