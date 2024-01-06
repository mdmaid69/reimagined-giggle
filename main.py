import os
def list_files_in_directory(path):
        return os.listdir(path)
import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a