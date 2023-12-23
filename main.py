def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)
import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)