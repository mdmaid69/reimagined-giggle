import shutil
def copy_file(src, dst):
        shutil.copy(src, dst)
import collections
def count_elements(iterable):
        return collections.Counter(iterable)