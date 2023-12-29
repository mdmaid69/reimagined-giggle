import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)
n = 10
print("Factorial numbers:", [1 if x == 0 else x * factorial(x - 1) for x in range(n)])