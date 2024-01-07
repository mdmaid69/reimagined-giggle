n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)