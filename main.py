def square_number(x):
        return x**2
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)