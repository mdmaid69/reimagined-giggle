import itertools
print(list(itertools.permutations([1, 2, 3])))
import shutil
def copy_file(src, dst):
        shutil.copy(src, dst)