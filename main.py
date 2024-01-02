import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)
def fibonacci(n):
        a, b = 0, 1
        while a < n:
        print(a, end=" ")
        a, b = b, a+b