text = "Hello, world!"
print("Uppercase:", text.upper())
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)