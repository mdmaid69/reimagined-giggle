import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)
n = 10
print("Powers of 2:", [2**x for x in range(n)])