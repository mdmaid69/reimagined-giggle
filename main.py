import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)
x = 10
y = 20
print("Sum:", x + y)