import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)
import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))