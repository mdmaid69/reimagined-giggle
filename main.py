import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)
def fibonacci(n):
        a, b = 0, 1
        while a < n:
        print(a, end=" ")
        a, b = b, a+b