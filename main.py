import array
def get_array_buffer_info(array):
        return array.buffer_info()
import shutil
def delete_directory(path):
        shutil.rmtree(path)