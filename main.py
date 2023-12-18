import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)
import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)