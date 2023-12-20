import itertools
print(list(itertools.permutations([1, 2, 3])))
import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)