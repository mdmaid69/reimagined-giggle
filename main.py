import collections
def count_elements(iterable):
        return collections.Counter(iterable)
import shutil
def copy_file(src, dst):
        shutil.copy(src, dst)