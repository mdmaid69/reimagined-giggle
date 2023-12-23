import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)
def calculate_area_rectangle(l, w):
        return l * w