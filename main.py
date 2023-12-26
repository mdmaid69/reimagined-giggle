import os
def list_files_in_directory(path):
        return os.listdir(path)
def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)