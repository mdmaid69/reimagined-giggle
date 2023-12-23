import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a
import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)