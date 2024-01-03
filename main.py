import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)
import math
def calculate_circle_area(radius):
        return math.pi * radius**2