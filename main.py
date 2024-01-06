import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)
import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))