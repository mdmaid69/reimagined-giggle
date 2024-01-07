import os
def list_files_in_directory(path):
        return os.listdir(path)
def calculate_energy(mass, c=3*10**8):
        return mass * c**2