import os
def get_file_size(filename):
        return os.path.getsize(filename)
import array
def get_array_buffer_info(array):
        return array.buffer_info()