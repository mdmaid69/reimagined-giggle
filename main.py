import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)
import os
def get_file_size(filename):
        return os.path.getsize(filename)