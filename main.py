n = 10
print("Fibonacci:", [((1 + 5**0.5) / 2)**n / 5**0.5 for n in range(n)])
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)