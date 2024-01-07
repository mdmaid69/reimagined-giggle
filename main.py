text = "Hello, world!"
print("Words:", len(text.split()))
import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)