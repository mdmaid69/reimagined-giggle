import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a
import shutil
def copy_file(src, dst):
        shutil.copy(src, dst)