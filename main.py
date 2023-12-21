import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)
name = "Python"
print("Hello,", name)