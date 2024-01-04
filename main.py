text = "Hello, world!"
print("Uppercase:", text.upper())
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)