def calculate_density(mass, volume):
        return mass / volume
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)