def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)
import json
def read_from_json(json_string):
        return json.loads(json_string)