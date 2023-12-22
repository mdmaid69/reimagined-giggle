import array
def get_string_from_array(array):
        return array.tobytes()
import os
def get_file_size(filename):
        return os.path.getsize(filename)