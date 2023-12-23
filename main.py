import glob
def find_files(pattern):
        return glob.glob(pattern)
import array
def get_array_typecode(array):
        return array.typecode