import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)
def calculate_density(mass, volume):
        return mass / volume