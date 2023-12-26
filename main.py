import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)
n = 10
print("Cube numbers:", [x**3 for x in range(n)])