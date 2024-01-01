import re
def split_string(pattern, string):
        return re.split(pattern, string)
import os
def get_file_size(filename):
        return os.path.getsize(filename)