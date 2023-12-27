import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)
def is_odd(n):
        return n % 2 != 0