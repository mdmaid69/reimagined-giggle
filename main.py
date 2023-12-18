import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a
import os
def remove_directory(path):
        os.rmdir(path)