import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
import shutil
def move_file(src, dst):
        shutil.move(src, dst)