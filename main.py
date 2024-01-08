import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)
print([x**2 for x in range(10)])