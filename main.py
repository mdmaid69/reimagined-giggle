import glob
def find_files(pattern):
        return glob.glob(pattern)
import array
def get_array_from_string(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a