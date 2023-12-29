def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)
import os
def remove_directory(path):
        os.rmdir(path)