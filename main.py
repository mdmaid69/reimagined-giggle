import re
def split_by_pattern(pattern, string):
        return re.split(pattern, string)
import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a