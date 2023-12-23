n = 10
print("Factorial numbers:", [1 if x == 0 else x * factorial(x - 1) for x in range(n)])
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)