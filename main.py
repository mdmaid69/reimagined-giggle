def calculate_acceleration(speed, time):
        return speed / time
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)