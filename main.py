import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))
import shutil
def move_file(src, dst):
        shutil.move(src, dst)