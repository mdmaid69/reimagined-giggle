import os
def remove_directory(path):
        os.rmdir(path)
def calculate_roi(gain, cost):
        return (gain - cost) / cost