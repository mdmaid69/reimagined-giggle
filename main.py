import os
def remove_directory(path):
        os.rmdir(path)
def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)