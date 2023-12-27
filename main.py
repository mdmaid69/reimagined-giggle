import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)
import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)