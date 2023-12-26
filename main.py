import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)
import array
def check_if_array_contains_item(array, item):
        return item in array