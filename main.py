text = "Hello, world!"
print("Is palindrome:", text == text[::-1])
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)