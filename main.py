def calculate_speed(distance, time):
        return distance / time
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)