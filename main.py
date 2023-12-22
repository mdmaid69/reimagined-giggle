import array
def get_array_as_bytes(array):
        return bytes(array)
import glob
def find_files(pattern):
        return glob.glob(pattern)