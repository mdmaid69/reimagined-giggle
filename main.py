import math
def calculate_cartesian_to_polar_coordinates(x, y):
        return math.rect(x, y)
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)