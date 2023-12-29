import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)
import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a