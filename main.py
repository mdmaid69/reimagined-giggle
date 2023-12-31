import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)
def calculate_area(radius):
        return 3.14 * radius * radius