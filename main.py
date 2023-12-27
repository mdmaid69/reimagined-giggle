import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)
import array
def get_array_from_bytes(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a