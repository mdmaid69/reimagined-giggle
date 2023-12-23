import re
def replace_pattern(pattern, replacement, string):
        return re.sub(pattern, replacement, string)
import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a