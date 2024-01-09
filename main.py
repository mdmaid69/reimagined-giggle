def calculate_speed(distance, time):
        return distance / time
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)