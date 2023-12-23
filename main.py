import os
def change_working_directory(path):
        os.chdir(path)
import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)