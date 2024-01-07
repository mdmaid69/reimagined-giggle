def fibonacci(n):
        a, b = 0, 1
        while a < n:
        print(a, end=" ")
        a, b = b, a+b
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)