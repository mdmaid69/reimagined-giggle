text = "Hello, world!"
print("Characters:", len(text))
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)