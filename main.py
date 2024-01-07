import array
def convert_array_to_unicode(array):
        return array.tounicode()
import re
def replace_all_occurrences(pattern, replacement, string):
        return re.sub(pattern, replacement, string)