import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)
import itertools
print(list(itertools.permutations([1, 2, 3])))