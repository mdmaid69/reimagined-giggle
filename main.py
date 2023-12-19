import array
def get_array_buffer_info(array):
        return array.buffer_info()
import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)