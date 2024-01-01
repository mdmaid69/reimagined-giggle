import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)
import array
def convert_array_to_unicode(array):
        return array.tounicode()