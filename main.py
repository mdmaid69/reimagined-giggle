n = 10
print("Cube numbers:", [x**3 for x in range(n)])
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)