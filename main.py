import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)
def calculate_perimeter_triangle(a, b, c):
        return a + b + c