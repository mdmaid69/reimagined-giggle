import os
def list_files_in_directory(path):
        return os.listdir(path)
def calculate_roi(gain, cost):
        return (gain - cost) / cost