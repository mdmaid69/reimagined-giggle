import os
def get_file_size(filename):
        return os.path.getsize(filename)
import array
def get_array_from_string(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a