import glob
def find_files(pattern):
        return glob.glob(pattern)
import array
def set_array_slice(array, i, j, iterable):
        array[i:j] = iterable