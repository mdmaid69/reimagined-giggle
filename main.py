import math
def calculate_sphere_volume(radius):
        return 4/3 * math.pi * radius**3
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)