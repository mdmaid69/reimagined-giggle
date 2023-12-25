import os
def get_file_size(filename):
        return os.path.getsize(filename)
def fibonacci(n):
        a, b = 0, 1
        while a < n:
        print(a, end=" ")
        a, b = b, a+b