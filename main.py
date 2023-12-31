import re
def replace_pattern(pattern, replacement, string):
        return re.sub(pattern, replacement, string)
import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)