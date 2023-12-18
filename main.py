import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
import shutil
def copy_file(src, dst):
        shutil.copy(src, dst)