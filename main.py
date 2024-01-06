import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)
def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)