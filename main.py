import glob
def find_files(pattern):
        return glob.glob(pattern)
import array
def get_array_from_bytes(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a