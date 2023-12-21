import glob
def find_files(pattern):
        return glob.glob(pattern)
import array
def get_array_slice(array, i, j):
        return array[i:j]