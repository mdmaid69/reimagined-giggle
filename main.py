import os
def list_files_in_directory(path):
        return os.listdir(path)
import re
def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)