import array
def get_bytes_from_array(array):
        return array.tobytes()
import os
def change_working_directory(path):
        os.chdir(path)