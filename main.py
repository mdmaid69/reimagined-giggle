import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)
def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)