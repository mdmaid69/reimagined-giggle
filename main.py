import math
def calculate_sphere_volume(radius):
        return 4/3 * math.pi * radius**3
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)