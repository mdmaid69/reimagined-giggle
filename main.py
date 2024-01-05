import os
def remove_directory(path):
        os.rmdir(path)
def calculate_energy(mass, c=3*10**8):
        return mass * c**2