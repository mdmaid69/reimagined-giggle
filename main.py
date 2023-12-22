import array
def convert_array_to_list(array):
        return array.tolist()
import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)