import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)
def calculate_roi(gain, cost):
        return (gain - cost) / cost