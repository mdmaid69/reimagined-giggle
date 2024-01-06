import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)
text = "Hello, world!"
print("Uppercase:", text.upper())