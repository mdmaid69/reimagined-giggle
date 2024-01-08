import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)
import re
def split_string(pattern, string):
        return re.split(pattern, string)