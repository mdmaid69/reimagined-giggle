import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)
import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a