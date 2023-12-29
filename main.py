import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a
import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)