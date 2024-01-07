import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)
text = "Hello, world!"
print("Reversed:", text[::-1])