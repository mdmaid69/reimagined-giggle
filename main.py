import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)
def calculate_area(radius):
        return 3.14 * radius * radius