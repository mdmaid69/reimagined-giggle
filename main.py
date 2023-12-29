import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)
def calculate_force(mass, acceleration):
        return mass * acceleration