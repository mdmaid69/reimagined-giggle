import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)
def calculate_pressure(force, area):
        return force / area