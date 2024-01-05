import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)
import os
def get_file_size(filename):
        return os.path.getsize(filename)