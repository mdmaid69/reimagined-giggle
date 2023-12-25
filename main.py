import os
def get_file_size(filename):
        return os.path.getsize(filename)
import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)