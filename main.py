import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)
def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)