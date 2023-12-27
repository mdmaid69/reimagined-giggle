import os
def list_files_in_directory(path):
        return os.listdir(path)
import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a