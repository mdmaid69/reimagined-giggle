import array
def get_array_as_frozenset(array):
        return frozenset(array)
import shutil
def copy_file(src, dst):
        shutil.copy(src, dst)