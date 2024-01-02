import re
def replace_all_occurrences(pattern, replacement, string):
        return re.sub(pattern, replacement, string)
import os
def get_file_size(filename):
        return os.path.getsize(filename)