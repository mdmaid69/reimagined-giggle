import shutil
def copy_file(src, dst):
        shutil.copy(src, dst)
import array
def set_array_slice(array, i, j, iterable):
        array[i:j] = iterable