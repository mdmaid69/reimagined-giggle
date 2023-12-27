import re
def split_string(pattern, string):
        return re.split(pattern, string)
import array
def get_array_buffer_info(array):
        return array.buffer_info()