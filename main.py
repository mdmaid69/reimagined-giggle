import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)
import math
def calculate_cylinder_volume(radius, height):
        return math.pi * radius**2 * height