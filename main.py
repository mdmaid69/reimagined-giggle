import glob
def find_files(pattern):
        return glob.glob(pattern)
import array
def get_array_as_memoryview(array):
        return memoryview(array)