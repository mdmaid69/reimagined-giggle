import array
def get_array_as_bytes(array):
        return bytes(array)
import shutil
def copy_file(src, dst):
        shutil.copy(src, dst)