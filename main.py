import math
def calculate_cone_volume(radius, height):
        return 1/3 * math.pi * radius**2 * height
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)