import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)
def cube_number(x):
        return x**3