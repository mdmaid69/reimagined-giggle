import re
def split_by_pattern(pattern, string):
        return re.split(pattern, string)
import os
def remove_directory(path):
        os.rmdir(path)