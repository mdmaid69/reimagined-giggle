import array
def get_array_as_memoryview(array):
        return memoryview(array)
import shutil
def copy_file(src, dst):
        shutil.copy(src, dst)