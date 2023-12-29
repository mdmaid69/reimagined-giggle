import array
def get_list_from_array(array):
        return array.tolist()
import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)