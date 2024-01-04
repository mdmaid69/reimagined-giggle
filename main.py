import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)
def calculate_perimeter_rectangle(l, w):
        return 2 * (l + w)