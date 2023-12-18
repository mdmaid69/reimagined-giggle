def calculate_pressure(force, area):
        return force / area
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)