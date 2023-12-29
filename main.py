import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)
def add_numbers(a, b):
        return a + b