import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a
import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)