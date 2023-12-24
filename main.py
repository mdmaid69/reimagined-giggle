import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)
import re
def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)