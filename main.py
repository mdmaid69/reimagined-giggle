import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)
import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a