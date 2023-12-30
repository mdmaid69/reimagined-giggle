import array
def get_array_as_bytes(array):
        return bytes(array)
import shutil
def move_file(src, dst):
        shutil.move(src, dst)