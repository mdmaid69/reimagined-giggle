import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)
def calculate_area_triangle(b, h):
        return 0.5 * b * h