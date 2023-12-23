text = "Hello, world!"
print("Is palindrome:", text == text[::-1])
import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)