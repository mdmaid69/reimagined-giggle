import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)
def calculate_power(work, time):
        return work / time