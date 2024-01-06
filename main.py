import glob
def find_files(pattern):
        return glob.glob(pattern)
import array
def insert_into_array(array, i, item):
        array.insert(i, item)