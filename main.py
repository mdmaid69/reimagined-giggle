import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)
import array
def convert_array_to_unicode(array):
        return array.tounicode()