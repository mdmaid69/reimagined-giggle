import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)
n = 10
print("Odd numbers:", [x for x in range(n) if x % 2 != 0])