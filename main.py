import glob
def find_files(pattern):
        return glob.glob(pattern)
import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a