import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)
import array
def get_array_from_string(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a