import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)
import math
def calculate_polar_to_cartesian_coordinates(r, theta):
        return math.polar((r, theta))