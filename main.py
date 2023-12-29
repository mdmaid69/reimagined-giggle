import os
def get_file_size(filename):
        return os.path.getsize(filename)
def calculate_volume(length, width, height):
        return length * width * height