import array
def get_string_from_array(array):
        return array.tobytes()
import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)