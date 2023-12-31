def calculate_volume(length, width, height):
        return length * width * height
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)