import shutil
def move_file(src, dst):
        shutil.move(src, dst)
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)