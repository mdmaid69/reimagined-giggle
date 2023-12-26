def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)