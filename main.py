import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)
import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)