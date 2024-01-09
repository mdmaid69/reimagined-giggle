import json
def read_from_json(json_string):
        return json.loads(json_string)
def calculate_density(mass, volume):
        return mass / volume