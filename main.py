import array
def get_bytes_from_array(array):
        return array.tobytes()
import glob
def find_files(pattern):
        return glob.glob(pattern)