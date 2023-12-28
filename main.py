import os
def list_files_in_directory(path):
        return os.listdir(path)
def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)