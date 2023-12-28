import shutil
def copy_file(src, dst):
        shutil.copy(src, dst)
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)