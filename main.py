def calculate_energy(mass, c=3*10**8):
        return mass * c**2
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)