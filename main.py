text = "Hello, world!"
print("Words:", len(text.split()))
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)