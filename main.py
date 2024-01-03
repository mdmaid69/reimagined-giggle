import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)
n = 10
print("Square numbers:", [x**2 for x in range(n)])