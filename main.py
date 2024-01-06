import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a
import glob
def find_files(pattern):
        return glob.glob(pattern)