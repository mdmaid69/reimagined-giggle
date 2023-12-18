import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)
n = 10
print("Prime numbers:", [x for x in range(2, n) if all(x % i != 0 for i in range(2, int(x**0.5) + 1))])