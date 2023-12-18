import os
def get_file_size(filename):
        return os.path.getsize(filename)
import re
def replace_pattern(pattern, replacement, string):
        return re.sub(pattern, replacement, string)