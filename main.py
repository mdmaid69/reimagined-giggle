import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)
print([x**2 for x in range(10)])