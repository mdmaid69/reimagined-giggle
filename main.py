import array
def get_array_from_bytes(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a
import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)