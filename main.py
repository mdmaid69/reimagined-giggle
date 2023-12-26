import glob
def find_files(pattern):
        return glob.glob(pattern)
import array
def extend_array(array, iterable):
        array.extend(iterable)