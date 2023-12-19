import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)
import os
def change_working_directory(path):
        os.chdir(path)