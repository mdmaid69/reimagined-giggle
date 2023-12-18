import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)
import math
def calculate_polar_to_cartesian_coordinates(r, theta):
        return math.polar((r, theta))