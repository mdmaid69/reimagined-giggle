import os
def change_working_directory(path):
        os.chdir(path)
import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))