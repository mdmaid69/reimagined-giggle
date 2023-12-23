import os
def get_file_size(filename):
        return os.path.getsize(filename)
def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)