import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)
def calculate_circumference_circle(r):
        return 2 * 3.14 * r