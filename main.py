n = 10
print("Is prime:", all(n % i != 0 for i in range(2, int(n**0.5) + 1)))
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)