import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)
import array
def get_list_from_array(array):
        return array.tolist()