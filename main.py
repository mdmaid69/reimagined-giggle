import array
def get_array_buffer_info(array):
        return array.buffer_info()
import os
def remove_directory(path):
        os.rmdir(path)