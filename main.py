import shutil
def move_file(src, dst):
        shutil.move(src, dst)
import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))