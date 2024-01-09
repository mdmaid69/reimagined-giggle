import array
def convert_array_to_bytes(array):
        return array.tobytes()
import os
def change_working_directory(path):
        os.chdir(path)