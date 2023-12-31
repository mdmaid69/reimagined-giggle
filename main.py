import shutil
def copy_file(src, dst):
        shutil.copy(src, dst)
import array
def get_array_from_bytes(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a