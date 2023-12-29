import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)
import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))