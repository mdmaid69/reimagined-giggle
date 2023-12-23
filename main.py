import json
def convert_to_json(data):
        return json.dumps(data)
text = "Hello, world!"
print("Is palindrome:", text == text[::-1])