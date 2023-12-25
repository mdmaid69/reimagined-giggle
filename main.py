import os
def list_files_in_directory(path):
        return os.listdir(path)
import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)