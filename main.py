text = "Hello, world!"
print("Is palindrome:", text == text[::-1])
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)