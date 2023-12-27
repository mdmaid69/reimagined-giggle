import os
def remove_directory(path):
        os.rmdir(path)
import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))