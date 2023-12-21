import os
def list_files_in_directory(path):
        return os.listdir(path)
import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a