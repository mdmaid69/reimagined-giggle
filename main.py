import os
def list_files_in_directory(path):
        return os.listdir(path)
def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)