def calculate_work(force, distance):
        return force * distance
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)