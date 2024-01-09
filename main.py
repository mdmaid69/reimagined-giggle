import os
def remove_directory(path):
        os.rmdir(path)
import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)