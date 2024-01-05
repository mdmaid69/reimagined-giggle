def fibonacci(n):
        a, b = 0, 1
        while a < n:
        print(a, end=" ")
        a, b = b, a+b
import json
def read_from_json(json_string):
        return json.loads(json_string)