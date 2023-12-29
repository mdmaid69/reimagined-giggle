import os
def remove_directory(path):
        os.rmdir(path)
def fibonacci(n):
        a, b = 0, 1
        while a < n:
        print(a, end=" ")
        a, b = b, a+b