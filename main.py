import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)
n = 10
print("Square numbers:", [x**2 for x in range(n)])