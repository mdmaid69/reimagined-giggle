def calculate_force(mass, acceleration):
        return mass * acceleration
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)