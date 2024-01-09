import array
def get_string_from_array(array):
        return array.tobytes()
import os
def remove_directory(path):
        os.rmdir(path)