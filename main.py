import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)
def calculate_volume(length, width, height):
        return length * width * height