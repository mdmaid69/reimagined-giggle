def fibonacci(n):
        a, b = 0, 1
        while a < n:
        print(a, end=" ")
        a, b = b, a+b
import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)