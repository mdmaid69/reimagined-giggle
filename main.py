import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)
def calculate_area(radius):
        return 3.14 * radius * radius