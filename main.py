import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))
import shutil
def copy_file(src, dst):
        shutil.copy(src, dst)