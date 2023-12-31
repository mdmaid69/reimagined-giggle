import array
def get_bytes_from_array(array):
        return array.tobytes()
import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)