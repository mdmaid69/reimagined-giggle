import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)
import array
def convert_array_to_bytes(array):
        return array.tobytes()