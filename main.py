def calculate_average(lst):
        return sum(lst) / len(lst)
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)