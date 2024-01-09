import array
def get_array_buffer_info(array):
        return array.buffer_info()
import shutil
def copy_file(src, dst):
        shutil.copy(src, dst)