import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)
import re
def replace_pattern(pattern, replacement, string):
        return re.sub(pattern, replacement, string)