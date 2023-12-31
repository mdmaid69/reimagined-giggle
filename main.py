import itertools
print(list(itertools.permutations([1, 2, 3])))
import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)