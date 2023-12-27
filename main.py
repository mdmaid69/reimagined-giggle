n = 10
print("Fibonacci:", [((1 + 5**0.5) / 2)**n / 5**0.5 for n in range(n)])
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)