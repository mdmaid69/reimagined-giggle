import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)
def calculate_pressure(force, area):
        return force / area