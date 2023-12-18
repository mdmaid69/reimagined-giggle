import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)
import math
def calculate_cylinder_volume(radius, height):
        return math.pi * radius**2 * height