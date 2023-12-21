def calculate_roi(gain, cost):
        return (gain - cost) / cost
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)