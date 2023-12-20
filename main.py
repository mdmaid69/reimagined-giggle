import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)
def greet(name):
        print(f"Hello, {name}!")