import os
def list_files_in_directory(path):
        return os.listdir(path)
import re
def replace_pattern(pattern, replacement, string):
        return re.sub(pattern, replacement, string)