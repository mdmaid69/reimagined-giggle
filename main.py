import os
def get_file_size(filename):
        return os.path.getsize(filename)
import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))