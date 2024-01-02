def calculate_area_circle(r):
        return 3.14 * r**2
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)