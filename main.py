import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)
n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)