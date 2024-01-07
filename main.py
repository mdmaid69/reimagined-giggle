import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a
import re
def split_string(pattern, string):
        return re.split(pattern, string)