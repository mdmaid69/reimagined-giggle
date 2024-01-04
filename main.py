import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)
def calculate_energy(mass, c=3*10**8):
        return mass * c**2