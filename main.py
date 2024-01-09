import collections
def count_elements(iterable):
        return collections.Counter(iterable)
import shutil
def move_file(src, dst):
        shutil.move(src, dst)