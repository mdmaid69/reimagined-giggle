import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)
import array
def get_bytes_from_array(array):
        return array.tobytes()