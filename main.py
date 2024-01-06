import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)
def greet(name):
        print(f"Hello, {name}!")