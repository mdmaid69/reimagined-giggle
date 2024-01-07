import shutil
def delete_directory(path):
        shutil.rmtree(path)
import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a