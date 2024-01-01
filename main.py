import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a
import os
def remove_directory(path):
        os.rmdir(path)