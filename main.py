import glob
def find_files(pattern):
        return glob.glob(pattern)
import itertools
print(list(itertools.permutations([1, 2, 3])))