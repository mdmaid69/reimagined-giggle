import os
def list_files_in_directory(path):
        return os.listdir(path)
import array
def get_array_from_bytes(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a