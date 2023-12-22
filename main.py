import array
def get_array_as_memoryview(array):
        return memoryview(array)
import shutil
def move_file(src, dst):
        shutil.move(src, dst)