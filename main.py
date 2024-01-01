import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)
def calculate_work(force, distance):
        return force * distance