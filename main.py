import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)
def calculate_speed(distance, time):
        return distance / time