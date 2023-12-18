import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)
def calculate_area_circle(r):
        return 3.14 * r**2