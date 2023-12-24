text = "Hello, world!"
print("Reversed:", text[::-1])
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)