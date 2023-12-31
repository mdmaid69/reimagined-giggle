import array
def get_bytes_from_array(array):
        return array.tobytes()
import os
def remove_directory(path):
        os.rmdir(path)