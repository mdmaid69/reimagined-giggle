import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)
import re
def split_by_pattern(pattern, string):
        return re.split(pattern, string)