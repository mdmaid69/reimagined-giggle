import shutil
def move_file(src, dst):
        shutil.move(src, dst)
import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))