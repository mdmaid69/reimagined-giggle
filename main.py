def calculate_volume(length, width, height):
        return length * width * height
import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)