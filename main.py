import re
def replace_pattern(pattern, replacement, string):
        return re.sub(pattern, replacement, string)
import os
def remove_directory(path):
        os.rmdir(path)