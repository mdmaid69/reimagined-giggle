import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)
def calculate_pressure(force, area):
        return force / area