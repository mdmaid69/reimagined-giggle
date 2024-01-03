import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))
import shutil
def copy_file(src, dst):
        shutil.copy(src, dst)