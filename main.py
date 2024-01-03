import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)
def convert_to_hex(n):
        return hex(n)