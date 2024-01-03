import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)
import os
def remove_directory(path):
        os.rmdir(path)