import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)
import array
def pop_from_array(array, i=-1):
        return array.pop(i)