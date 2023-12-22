import array
def get_string_from_array(array):
        return array.tobytes()
import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)