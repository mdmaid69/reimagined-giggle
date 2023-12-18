import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)
def calculate_acceleration(speed, time):
        return speed / time