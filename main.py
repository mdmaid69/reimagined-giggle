import array
def set_array_slice(array, i, j, iterable):
        array[i:j] = iterable
import shutil
def delete_directory(path):
        shutil.rmtree(path)