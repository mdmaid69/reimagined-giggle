import json
def read_from_json(json_string):
        return json.loads(json_string)
text = "Hello, world!"
print("Is palindrome:", text == text[::-1])