def fibonacci(n):
        a, b = 0, 1
        while a < n:
        print(a, end=" ")
        a, b = b, a+b
import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)