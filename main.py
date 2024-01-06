import json
def read_from_json(json_string):
        return json.loads(json_string)
def calculate_energy(mass, c=3*10**8):
        return mass * c**2