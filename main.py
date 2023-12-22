import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))
import glob
def find_files(pattern):
        return glob.glob(pattern)