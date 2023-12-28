import os
def change_working_directory(path):
        os.chdir(path)
import array
def get_array_buffer_info(array):
        return array.buffer_info()