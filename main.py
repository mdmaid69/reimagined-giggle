import glob
def find_files(pattern):
        return glob.glob(pattern)
import array
def remove_from_array(array, item):
        array.remove(item)