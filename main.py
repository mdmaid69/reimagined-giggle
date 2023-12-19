import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)
import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)