import array
def get_array_as_frozenset(array):
        return frozenset(array)
import shutil
def move_file(src, dst):
        shutil.move(src, dst)