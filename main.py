import array
def convert_array_to_bytes(array):
        return array.tobytes()
import os
def remove_directory(path):
        os.rmdir(path)