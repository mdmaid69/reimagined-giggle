import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))
import shutil
def copy_file(src, dst):
        shutil.copy(src, dst)