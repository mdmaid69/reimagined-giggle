import os
def get_current_working_directory():
        return os.getcwd()
def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)