import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)
import array
def get_array_buffer_info(array):
        return array.buffer_info()