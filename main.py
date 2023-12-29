import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)
import os
def remove_directory(path):
        os.rmdir(path)