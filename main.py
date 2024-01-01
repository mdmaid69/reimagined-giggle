def calculate_energy(mass, c=3*10**8):
        return mass * c**2
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)