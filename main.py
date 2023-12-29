import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)
def calculate_density(mass, volume):
        return mass / volume