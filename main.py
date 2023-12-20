import json
def read_from_json(json_string):
        return json.loads(json_string)
def greet(name):
        print(f"Hello, {name}!")