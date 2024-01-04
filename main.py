import sys
def add_to_python_path(path):
        sys.path.append(path)
import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a