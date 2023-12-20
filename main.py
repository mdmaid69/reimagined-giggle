import array
def get_array_buffer_info(array):
        return array.buffer_info()
import re
def replace_all_occurrences(pattern, replacement, string):
        return re.sub(pattern, replacement, string)