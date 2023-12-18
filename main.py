import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)
import math
def calculate_degrees_to_radians(degrees):
        return math.radians(degrees)