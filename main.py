import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)
import re
def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)