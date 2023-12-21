import os
def get_file_size(filename):
        return os.path.getsize(filename)
import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a