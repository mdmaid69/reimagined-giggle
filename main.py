import os
def list_files_in_directory(path):
        return os.listdir(path)
import re
def replace_all_occurrences(pattern, replacement, string):
        return re.sub(pattern, replacement, string)