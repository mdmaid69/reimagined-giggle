import re
def replace_pattern(pattern, replacement, string):
        return re.sub(pattern, replacement, string)
import array
def check_if_array_contains_item(array, item):
        return item in array