def calculate_area(radius):
        return 3.14 * radius * radius
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)