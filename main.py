import array
def convert_array_to_bytes(array):
        return array.tobytes()
import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)