import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)
def calculate_area_circle(r):
        return 3.14 * r**2