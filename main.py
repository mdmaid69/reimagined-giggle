import array
def convert_array_to_unicode(array):
        return array.tounicode()
import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)