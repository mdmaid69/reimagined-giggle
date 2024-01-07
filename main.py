import array
def get_string_from_array(array):
        return array.tobytes()
import glob
def find_files(pattern):
        return glob.glob(pattern)