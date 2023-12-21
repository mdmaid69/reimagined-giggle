import os
def get_file_size(filename):
        return os.path.getsize(filename)
def calculate_pressure(force, area):
        return force / area