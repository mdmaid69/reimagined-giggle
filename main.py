import itertools
print(list(itertools.permutations([1, 2, 3])))
import shutil
def move_file(src, dst):
        shutil.move(src, dst)