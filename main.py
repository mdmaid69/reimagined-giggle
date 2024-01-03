import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)
import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a