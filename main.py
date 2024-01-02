import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)
import math
def calculate_circle_circumference(radius):
        return 2 * math.pi * radius