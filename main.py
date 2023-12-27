import array
def get_array_as_format(array, format_spec):
        return format(array, format_spec)
import re
def replace_pattern(pattern, replacement, string):
        return re.sub(pattern, replacement, string)