import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)
def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)