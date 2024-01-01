import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)
def calculate_energy(mass, c=3*10**8):
        return mass * c**2