import json
def convert_to_json(data):
        return json.dumps(data)
def calculate_energy(mass, c=3*10**8):
        return mass * c**2