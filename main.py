import os
def get_file_size(filename):
        return os.path.getsize(filename)
def calculate_perimeter_rectangle(l, w):
        return 2 * (l + w)