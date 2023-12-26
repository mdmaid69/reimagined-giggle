import array
def get_array_buffer_info(array):
        return array.buffer_info()
import glob
def find_files(pattern):
        return glob.glob(pattern)