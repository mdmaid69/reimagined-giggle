import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)
import re
def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)