import array
def get_bytes_from_array(array):
        return array.tobytes()
import os
def list_files_in_directory(path):
        return os.listdir(path)