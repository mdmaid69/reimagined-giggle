import re
def split_by_pattern(pattern, string):
        return re.split(pattern, string)
import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)