import array
def set_array_slice(array, i, j, iterable):
        array[i:j] = iterable
import shutil
def move_file(src, dst):
        shutil.move(src, dst)