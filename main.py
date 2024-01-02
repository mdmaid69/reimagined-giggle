def calculate_area(radius):
        return 3.14 * radius * radius
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)