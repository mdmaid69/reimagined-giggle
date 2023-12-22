import re
def split_by_pattern(pattern, string):
        return re.split(pattern, string)
import os
def list_files_in_directory(path):
        return os.listdir(path)