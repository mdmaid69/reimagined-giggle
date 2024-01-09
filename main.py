import os
def list_files_in_directory(path):
        return os.listdir(path)
import array
def get_array_from_string(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a