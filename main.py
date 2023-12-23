import math
def calculate_circle_circumference(radius):
        return 2 * math.pi * radius
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)