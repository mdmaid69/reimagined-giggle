import re
def split_by_pattern(pattern, string):
        return re.split(pattern, string)
import os
def get_file_size(filename):
        return os.path.getsize(filename)