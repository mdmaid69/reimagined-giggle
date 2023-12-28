import shutil
def delete_directory(path):
        shutil.rmtree(path)
import array
def get_array_from_bytes(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a