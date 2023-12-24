import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)
def is_even(n):
        return n % 2 == 0