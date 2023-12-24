import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)
import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a