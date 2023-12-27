def calculate_volume(length, width, height):
        return length * width * height
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)