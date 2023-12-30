import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)
x = 10
y = 20
print("Sum:", x + y)