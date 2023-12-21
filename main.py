import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)
import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a