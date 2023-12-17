import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)
def calculate_density(mass, volume):
        return mass / volume