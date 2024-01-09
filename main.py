import os
def list_files_in_directory(path):
        return os.listdir(path)
def calculate_average(lst):
        return sum(lst) / len(lst)