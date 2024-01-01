def calculate_density(mass, volume):
        return mass / volume
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)