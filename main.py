import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)
def calculate_area(radius):
        return 3.14 * radius * radius