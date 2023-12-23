def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)
import os
def change_working_directory(path):
        os.chdir(path)