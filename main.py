import array
def get_array_buffer_info(array):
        return array.buffer_info()
import re
def split_by_pattern(pattern, string):
        return re.split(pattern, string)