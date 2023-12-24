import os
def remove_directory(path):
        os.rmdir(path)
import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)