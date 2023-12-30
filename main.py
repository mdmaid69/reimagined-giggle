n = 10
print("Powers of 2:", [2**x for x in range(n)])
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)