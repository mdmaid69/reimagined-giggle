import re
def replace_pattern(pattern, replacement, string):
        return re.sub(pattern, replacement, string)
import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)