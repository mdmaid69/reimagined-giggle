import array
def get_array_from_bytes(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a
import shutil
def move_file(src, dst):
        shutil.move(src, dst)