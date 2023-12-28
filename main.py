import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)
def calculate_work(force, distance):
        return force * distance