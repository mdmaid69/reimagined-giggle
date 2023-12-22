import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)
def calculate_area_triangle(b, h):
        return 0.5 * b * h