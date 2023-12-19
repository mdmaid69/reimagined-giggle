import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)
import os
def list_files_in_directory(path):
        return os.listdir(path)