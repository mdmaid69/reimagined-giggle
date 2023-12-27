import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)
import os
def list_files_in_directory(path):
        return os.listdir(path)