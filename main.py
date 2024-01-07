def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)