import array
def convert_array_to_bytes(array):
        return array.tobytes()
import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)