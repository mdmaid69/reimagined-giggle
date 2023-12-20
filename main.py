import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)
def calculate_roi(gain, cost):
        return (gain - cost) / cost