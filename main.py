import itertools
print(list(itertools.permutations([1, 2, 3])))
import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)